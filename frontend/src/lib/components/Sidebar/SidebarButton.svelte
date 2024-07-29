<script lang="ts">
	const { icon }: { icon: string } = $props();
</script>

<button on:click class="p-6">
	<i class="fa-solid {icon} fa-xl"/>
</button>