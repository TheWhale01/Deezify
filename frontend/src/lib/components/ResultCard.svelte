<script lang="ts">
  import type SearchResult from "$lib/types/search_results";

	const { item }: { item: SearchResult } = $props();

	function add_to_queue(item: SearchResult) {
		console.log(item);
	}
</script>

<button on:click={() => add_to_queue(item)}>
	<div class="flex flex-col justify-center items-center">
		<img class="rounded-lg" src={item.cover} alt="album cover" />
		<h1>{item.title}</h1>
		<span>Artist: {item.artist}</span>
	</div>
</button>