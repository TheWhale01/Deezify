<script lang="ts">
	import { setNotification } from "$lib/components/Notifier/Notifier.svelte";
	import Notifications from "$lib/components/Notifier/Notifications.svelte";
	import Sidebar from "$lib/components/Sidebar/Sidebar.svelte";
	import '@fortawesome/fontawesome-free/css/all.min.css'
	import { setPlayer, setUser } from "$lib/store.svelte";
	import Services from "$lib/enums/services";
	import PlayState from "$lib/enums/play_state";
	import env from "$lib/env";
	import { onMount } from "svelte";
	import { socket } from "$lib/socket";

	const notifier = setNotification();
	const { children } = $props();
	const user = setUser();
	const playerbar = setPlayer();
	let song_removed: boolean = $state(false);

	socket.on('track_removed', () => {
	 console.log("bonsoir je ne suis pas moi !");
	 playerbar.songs.shift();
	});

	socket.on('track_added', (data: string) => {
		playerbar.songs.push(data);
	});

	onMount(async () => {
		await user.get_me();
		await user.get_party_owner();
		if (user.owner && user.service === Services.SPOTIFY)
			initSpotifyPlayback();
	})

	async function setDeviceId(device_id: string): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/party/device_id?device_id=${device_id}`, {
			method: 'POST',
			credentials: 'include',
		});
		if (response.status !== 200)
			return;
	}

	function initSpotifyPlayback() {
		window.onSpotifyWebPlaybackSDKReady = () => {
			const player = new Spotify.Player({
				name: 'Deezify',
				getOAuthToken: cb => { cb(user.token) },
				volume: 1,
			});
			playerbar.player = player;
			player.addListener('not_ready', (message) => { console.log(message); notifier.add("Playback", message, 'error'); });
			player.addListener('account_error', (message) => { console.log(message); notifier.add("Playback", message, 'error');});
			player.addListener('playback_error', (message) => { console.log(message); notifier.add("Playback", message, 'error');});

			player.addListener('ready', async ({ device_id }: {device_id: string}) => {
				playerbar.device_id = device_id;
				await setDeviceId(device_id);
			});

			player.addListener('player_state_changed', async ({ paused, track_window: { current_track } }) => {
				switch (paused) {
					case true:
						playerbar.state = PlayState.PAUSED;
						break;
					case false:
						playerbar.state = PlayState.PLAYING
						break;
					default:
						playerbar.state = PlayState.LOADING;
						break;
				}
				if (song_removed && current_track.id === playerbar.current_song?.song_id) {
					song_removed = false;
				}
				if (!song_removed && current_track.id !== playerbar.current_song?.song_id) {
					playerbar.remove_song();
					socket.emit('remove_track', { party_id: user.party_id });
					song_removed = true;
				}
			});
			player.connect();
		}
	}


</script>

<svelte:head>
	{#if user.owner && user.service === Services.SPOTIFY}
		<script src="https://sdk.scdn.co/spotify-player.js"></script>
	{/if }
</svelte:head>

<Sidebar/>
<Notifications />

<div class="flex flex-col flex-1 justify-around items-center overflow-scroll">
	 {@render children()}
</div>
