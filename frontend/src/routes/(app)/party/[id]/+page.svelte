<script lang="ts">
	import type Party from "$lib/types/party";
	import env from "$lib/env";
	import { goto } from "$app/navigation";
	import type SearchResult from "$lib/types/search_results";

	export let data: Party;
	export let form: any;

	const results: SearchResult[] | null = form?.data;
	async function delete_party(): Promise<void> {
		const response = await fetch(
			env.BACKEND_URL + `/party/${data.id}`,
			{
				method: "DELETE",
				credentials: "include",
			},
		);
		if (response.status !== 200) return;
		goto('/');
	}
</script>

<h2>Party</h2>

<form method="post">
	<input type="text" placeholder="Search" name="search">
	<button type="submit">Search</button>
</form>

{#if results}
	<div>
		{#each results as item}
			<span>{item.id}</span>
			<span>{item.title}</span>
			<span>{item.artist}</span>
			<img src="{item.cover}" alt="album cover">
		{/each}
	</div>
{/if}
<!-- show the delete button if the connected user is the admin of this party -->
<button on:click={delete_party}>Delete</button>
