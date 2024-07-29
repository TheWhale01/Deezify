<script lang="ts">
  import type SearchResult from "$lib/types/search_results";

	const { item }: { item: SearchResult } = $props();

	function add_to_queue(item: SearchResult) {
		console.log(item);
	}
</script>

<button on:click={() => add_to_queue(item)}>
	<span>{item.id}</span>
	<span>{item.title}</span>
	<span>{item.artist}</span>
	<img class="rounded-lg" src={item.cover} alt="album cover" />
</button>