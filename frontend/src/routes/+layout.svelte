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

	const notifier = setNotification();
	const { children } = $props();
	const user = setUser();
	const playerbar = setPlayer();

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
			player.addListener('not_ready', (message) => { console.err(message); notifier.add("Playback", message, 'error'); });
			player.addListener('account_error', (message) => { console.err(message); notifier.add("Playback", message, 'error');});
			player.addListener('playback_error', (message) => { console.err(message); notifier.add("Playback", message, 'error');});

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
				if (current_track.id !== playerbar.current_song?.song_id)
					playerbar.songs.shift();
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
