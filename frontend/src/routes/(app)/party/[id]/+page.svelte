<script lang="ts">
	import SidebarButton from '$lib/components/Sidebar/SidebarButton.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
    	import type Track from '$lib/types/track.js';
	import { onMount } from 'svelte';
    import env from '$lib/env.js';

	const { data } = $props();

	let spotify_device_id: string = $state('');
	const songs: Track[] = $state(data['songs']);
	const current_song: Track = $derived(songs[0]);

	onMount(() => {
		$effect(() => {
			if (current_song)
				initSpotifyPlayback();
		});
	});

	async function setSong(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/song/init_playback?device_id=${spotify_device_id}&song_id=${current_song.song_id}`, {
			method: "PUT",
			credentials: 'include'
		});
		if (response.status !== 200)
			return ;
		console.log(await response.json());
	}

	function initSpotifyPlayback() {
		window.onSpotifyWebPlaybackSDKReady = () => {
			const player = new Spotify.Player({
				name: 'Deezify',
				getOAuthToken: cb => { cb(current_song.added_by.token) },
				volume: 1,
			});

			player.addListener('ready', async ({ device_id }: {device_id: string}) => {
				spotify_device_id = device_id;
				await setSong();
				player.togglePlay();
			});
			player.connect();
		}
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
