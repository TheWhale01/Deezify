<script lang="ts">
	import SidebarButton from '$lib/components/Sidebar/SidebarButton.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
    	import type Track from '$lib/types/track.js';
	import { owner, spotify_loaded, spotify_device_id } from '$lib/store.svelte.js';
	import { onMount } from 'svelte';

	const { data } = $props();

	const songs: Track[] = $state(data['songs']);
	const current_song: Track = $derived(songs[0]);

	onMount(() => {
		$effect(() => {
			if (owner.value && !spotify_loaded.value) {
				importSpotifyPlayback();
				if (current_song)
					initSpotifyPlayback();
			}
		});
	});

	function initSpotifyPlayback() {
		window.onSpotifyWebPlaybackSDKReady = () => {
			const player = new Spotify.Player({
				name: 'Deezify',
				getOAuthToken: cb => { cb(current_song.added_by.token) },
				volume: 1,
			});

			player.addListener('ready', ({ device_id }: {device_id: string}) => {
				if (spotify_device_id)
					return ;
				spotify_device_id.value = device_id;
				player.togglePlay();
			});
			player.connect();
		}
	}

	function importSpotifyPlayback() {
		const script = document.createElement('script');
		script.src = 'https://sdk.scdn.co/spotify-player.js';
		script.onload = () => spotify_loaded.value = true;
		document.body.appendChild(script);
	}
	
	async function delete_song(song: Track): Promise<void> {
		console.log(song);
		console.log('WIP');
	}
</script>


<h2>Now playing</h2>
{#if current_song}
	<ResultCard item={current_song} />
{/if }
<div class="flex flex-col">
	<h2>Queue</h2>
	{#if songs && songs.length}
		{#each songs as song }
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
		{/each }
	{/if }
</div>
