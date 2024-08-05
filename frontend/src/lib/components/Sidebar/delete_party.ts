import env from "$lib/env";


export default async function delete_party(pathname: string): Promise<void> {
	const response = await fetch(env.BACKEND_URL + pathname, {
		method: "DELETE",
		credentials: "include",
	});
	if (response.status !== 200) return;
	window.location.reload();
}
