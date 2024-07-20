import { redirect } from '@sveltejs/kit';

export const handle = async ({ event, resolve }: any) => {
	const token: string | undefined = event.cookies.get('access_token');

	if (!token && !event.route.id?.startsWith('/login'))
		throw redirect(302, '/login');
	else if (token && !event.route.id?.startsWith('/(app)'))
		throw redirect(302, '/');
	const response = await resolve(event);
	return response;
}
