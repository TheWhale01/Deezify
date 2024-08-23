<script lang="ts">
	const { icon }: { icon: string } = $props();
</script>

<div class="p-6">
	<button on:click>
		<i class="fa-solid {icon} fa-xl"></i>
	</button>
</div>
