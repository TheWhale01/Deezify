import env from "$lib/env";

export default async function logout(): Promise<void> {
	const response = await fetch(env.BACKEND_URL + `/user/logout`, {
		method: "DELETE",
		credentials: "include",
	});
	if (response.status !== 200) return;
	window.location.reload();
}