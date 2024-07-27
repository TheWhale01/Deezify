import env from "$lib/env";
import { redirect } from "@sveltejs/kit";

export const handle = async ({ event, resolve }: any) => {
	const token: string | undefined = event.cookies.get("access_token");
	const cookie_string: string = `access_token=${token}`;
	const user_response = await fetch(env.SERVER_BACKEND_URL + "/user/me", {
		method: "GET",
		headers: {
			Cookie: cookie_string,
		},
	});
	const valid_token: boolean = user_response.status === 200;
	if (!valid_token)
		event.cookies.delete("access_token", {
			path: "/",
		});

	if ((!token || !valid_token) && !event.route.id?.startsWith("/login"))
		throw redirect(302, "/login");
	else if (token && !event.route.id?.startsWith("/(app)"))
		throw redirect(302, "/");
	const response = await resolve(event);
	return response;
};
