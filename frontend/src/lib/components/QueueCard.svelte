<script lang="ts">
	import type Track from "$lib/types/track";
	import SidebarButton from "./Sidebar/SidebarButton.svelte";

	const { track }: { track: Track } = $props();

	async function delete_from_queue(): Promise<void> {
		console.log("bonsoir je ne suis pas moi !");
		// const response = await fetch(env.BACKEND_URL + '');
		// if (response.status !== 200)
		// 	return ;
	}
</script>
<div class="bg-slate-200 p-4 rounded shadow-md flex items-center justify-between mb-4">
	<img class="w-1/4 h-auto rounded" src={track.cover} alt="album cover" />
	<h1>{track.title}</h1>
	<span>Artist: {track.artist}</span>
	<span>Added By: {track.added_by.username}</span>
	<SidebarButton on:click={delete_from_queue} icon="fa-trash" />
</div>
