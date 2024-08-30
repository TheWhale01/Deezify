<script lang="ts">
	import Player from '$lib/components/Player.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
	import env from '$lib/env.js';
	import { getPlayer, getUser } from '$lib/store.svelte.js';
	import Services from '$lib/enums/services.js';
	import Deezer from '$lib/components/Deezer.svelte';
	import PlayState from '$lib/enums/play_state.js';
	import QueueCard from '$lib/components/QueueCard.svelte';
	import { onMount } from 'svelte';

	const { data } = $props();

	const player = getPlayer();
	player.songs = data['songs'];
	const user = getUser();
	
	onMount(() => {
		if (player.state === PlayState.PLAYING)
			return ;
		$effect(() => {
			setSong();
		})
	});
	
	async function setSong(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/song/init_playback?song_id=${player.songs.length >= 1 ? player.current_song.song_id : null}`, {
			method: "PUT",
			credentials: 'include'
		});
		if (response.status !== 200)
			return ;
	}
</script>

{#if user.service === Services.DEEZER }
	<Deezer />
{/if}

<h2>Now playing</h2>
{#if player.current_song}
	<ResultCard item={player.current_song} />
{/if }

<div class="flex flex-col w-[90%]">
<h2 class="text-center">Queue</h2>
	{#if player.songs && player.songs.length}
		{#each player.songs as song}
			{#if song != player.current_song }
				<QueueCard track={song} />
			{/if }
		{/each }
	{/if }
</div>

{#if user.owner}
	<Player />
{/if }
