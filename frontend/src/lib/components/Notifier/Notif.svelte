<script lang="ts">
	import type Notification from "$lib/types/notification";
	import { getNotification } from "./Notifier.svelte";
	import { fade } from "svelte/transition";

	const { notif }: { notif: Notification } = $props();
	const notifier = getNotification();
	
	let style = $state('rounded-lg flex flex-col text-center justify-center shadow-md w-full h-[10%] ');
	let background_color: string = '';
	switch (notif.type) {
		case "success":
			background_color = "hover:bg-green-600 bg-green-500";
			break;
		case "error":
			background_color = "hover:bg-red-600 bg-red-500";
			break;
		default:
			background_color = "hover:bg-blue-600 bg-blue-500";
			break;
	}
	style += background_color;
</script>

<button in:fade={{ duration: 500 }} out:fade={{ duration: 500 }} class={style} onclick={() => {notifier.remove(notif.id);}}>
	<p class="font-bold">{notif.title}</p>
	<p class="font-semibold">{notif.message}</p>
</button>
