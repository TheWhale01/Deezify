<script lang="ts">
	import env from "$lib/env";
	import type SearchResult from "$lib/types/search_results";
	import { getNotification } from "./Notifier/Notifier.svelte";

	const { item }: { item: SearchResult } = $props();

	const notifier = getNotification();
	async function add_to_queue(item: SearchResult): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/song?song_id=${item.id}`, {
			method: 'POST',
			credentials: 'include',
		});
		if (response.status !== 200 && response.status !== 204) {
			notifier.add('Add to queue', `Could not add to queue: ${response.text}`, 'error');
			return;
		}
		notifier.add('Add to queue', `${item.title} added to queue`, 'success');
	}
</script>

<button onclick={() => add_to_queue(item)}>
	<div class="flex flex-col justify-center items-center">
		<img class="rounded-lg" src={item.cover} alt="album cover" />
		<h1>{item.title}</h1>
		<span>Artist: {item.artist}</span>
	</div>
</button>
