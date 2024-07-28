<script lang="ts">
	import Sidebar from "$lib/components/Sidebar.svelte";
	import { sidebar } from "$lib/store";
</script>

<Sidebar logged={ $sidebar } />

<div class="flex flex-col flex-1 justify-around items-center overflow-scroll">
	<slot></slot>
</div>
