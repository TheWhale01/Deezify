<script lang="ts">
	import Sidebar from "$lib/components/Sidebar/Sidebar.svelte";
	import '@fortawesome/fontawesome-free/css/all.min.css'
	import { setPlayer, setUser } from "$lib/store.svelte";
  import Services from "$lib/enums/services";
    import { onMount } from "svelte";
		import PlayState from "$lib/enums/play_state";

	const { children } = $props();
	const user = setUser();
	const playerbar = setPlayer();

	onMount(() => {
		initSpotifyPlayback();	
	});

	function initSpotifyPlayback() {
		window.onSpotifyWebPlaybackSDKReady = () => {
			const player = new Spotify.Player({
				name: 'Deezify',
				getOAuthToken: cb => { cb(user.token) },
				volume: 1,
			});

			player.addListener('ready', async ({ device_id }: {device_id: string}) => {
				playerbar.device_id = device_id;
				console.log(device_id);
				player.activateElement()
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

<div class="flex flex-col flex-1 justify-around items-center overflow-scroll">
	 {@render children()}
</div>
