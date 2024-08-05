import env from "$lib/env";
import { spotify_device_id, spotify_loaded } from "$lib/store.svelte";


export default async function delete_party(pathname: string): Promise<void> {
	const response = await fetch(env.BACKEND_URL + pathname, {
		method: "DELETE",
		credentials: "include",
	});
	if (response.status !== 200) return;
	spotify_loaded.value = false;
	spotify_device_id.value = '';
	window.location.reload();
}
