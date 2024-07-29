import env from "$lib/env";
import { goto } from "$app/navigation";
// import { party_id } from "$lib/store.svelte";

export default async function delete_party(): Promise<void> {
	let party_id_value: number = 0;
	// party_id.subscribe((value) => {party_id_value = value});
	const response = await fetch(env.BACKEND_URL + `/party/${party_id_value}`, {
		method: "DELETE",
		credentials: "include",
	});
	if (response.status !== 200) return;
	goto("/");
}