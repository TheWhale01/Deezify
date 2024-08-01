<script lang="ts">
	import SidebarButton from '$lib/components/Sidebar/SidebarButton.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';

	const { data } = $props();

	const songs = data['songs'];
	let current_song = songs[0];
	
	async function delete_song(song): Promise<void> {
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
						<p>{song.added_by_user}</p>
					</div>
				</div>
				<SidebarButton on:click={() => {delete_song(song)}} icon="fa-trash"/>
			</div>
		{/each }
	{/if }
</div>
