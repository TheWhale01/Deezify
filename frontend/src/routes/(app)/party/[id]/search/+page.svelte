<script lang="ts">
	import type SearchResult from "$lib/types/search_results";

	export let form: any;

	const results: SearchResult[] | null = form?.data;
	
	async function add_to_queue(item: SearchResult): Promise<void> {
		console.log(item);
	}
</script>

<form method="post">
	<input type="text" placeholder="Search" name="search" />
	<button type="submit">Search</button>
</form>

{#if results}
	<div>
		<ul>
			{#each results as item}
				<li>
					<button on:click={() => add_to_queue(item)}>
						<span>{item.id}</span>
						<span>{item.title}</span>
						<span>{item.artist}</span>
						<img src={item.cover} alt="album cover" />
					</button>
				</li>
			{/each}
		</ul>
	</div>
{/if}