<script lang="ts">
	import Player from '$lib/components/Player.svelte';
	import SidebarButton from '$lib/components/Sidebar/SidebarButton.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
	import type Track from '$lib/types/track';
	import { onMount } from 'svelte';
	import env from '$lib/env.js';
	import { getPlayer, getUser } from '$lib/store.svelte.js';
	import Services from '$lib/enums/services.js';
	import Deezer from '$lib/components/Deezer.svelte';
  import PlayState from '$lib/enums/play_state.js';

	const { data } = $props();

	const playerbar = getPlayer();
	const user = getUser();
	const songs: Track[] = $state(data['songs']);
	const current_song: Track = $derived(songs[0]);

	onMount(() => {
		switch(user.service) {
			case Services.SPOTIFY:
				initSpotifyPlayback();
				if (playerbar.state !== PlayState.PLAYING)
					setSong();
				break;
			case Services.DEEZER:
				console.log("bonsoir je ne suis pas moi");
				break; 
			default:
				break;
		}
	});

	async function setSong(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/song/init_playback?device_id=${playerbar.device_id}`, {
			method: "PUT",
			credentials: 'include'
		});
		if (response.status !== 200)
			return ;
	}

	function initSpotifyPlayback() {
		window.onSpotifyWebPlaybackSDKReady = () => {
			const player = new Spotify.Player({
				name: 'Deezify',
				getOAuthToken: cb => { cb(user.token) },
				volume: 1,
			});

			player.addListener('ready', async ({ device_id }: {device_id: string}) => {
				playerbar.device_id = device_id;
				player.togglePlay();
				player.activateElement()
			});

			player.addListener('player_state_changed', async ({ paused, track_window: { current_track } }) => {
				if (current_song && current_track.id !== current_song.song_id)
					songs.shift();
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

	async function delete_song(song: Track): Promise<void> {
		console.log(song);
		console.log('WIP');
	}
</script>

{#if user.service === Services.DEEZER }
	<Deezer />
{/if}

<h2>Now playing</h2>
{#if current_song}
	<ResultCard item={current_song} />
{/if }
<div class="flex flex-col">
<h2>Queue</h2>
	{#if songs && songs.length}
		{#each songs as song}
			{#if song != current_song }
				<div>
					<div>
						<img src={song.cover} alt="album cover" />
						<div>
							<h2>{song.title}</h2>
							<p>{song.artist}</p>
							<span>Added By:</span>
							<p>{song.added_by.username}</p>
						</div>
					</div>
					<SidebarButton on:click={() => {delete_song(song)}} icon="fa-trash"/>
				</div>
			{/if }
		{/each }
	{/if }
</div>

<Player />
