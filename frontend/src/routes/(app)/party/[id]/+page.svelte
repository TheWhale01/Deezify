<script lang="ts">
	import type Party from "$lib/types/party";
	export let data: Party;
</script>

<h2>Party</h2>

<p>id: {data.id}</p>
<p>owner_id: {data.owner_id}</p>
<p>name: {data.name}</p>

<!-- show the delete button if the connected user is the admin of this party -->
