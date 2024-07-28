<script lang="ts">
	import { sidebar } from "$lib/store";
	import { onMount } from "svelte";

	onMount(() => { $sidebar = true });
</script>

<slot></slot>
