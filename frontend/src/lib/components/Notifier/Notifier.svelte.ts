import type Notification from '$lib/types/notification';
import { getContext, onDestroy, setContext } from 'svelte';

export class Notifier {
	notifications = $state<Notification[]>([]);
	timeoutMap = new Map<string, number>();

	constructor() {
		onDestroy(() => {
			for (const timeout of this.timeoutMap.values())
				clearTimeout(timeout);
			this.timeoutMap.clear();
		});
	}

	add(title: string, message: string, type: 'success' | 'error' | 'info', duration: number = 5000) {
		const id = crypto.randomUUID();
		this.notifications.push({
			id: id,
			title: title,
			message: message,
			type: type,
		});
		this.timeoutMap.set(
			id,
			setTimeout(() => {
				this.remove(id);
			}, duration)
		);
	}
	
	remove(id: string) {
		const timeout = this.timeoutMap.get(id);
		if (timeout) {
			clearTimeout(timeout);
			this.timeoutMap.delete(id);
		}
		this.notifications = this.notifications.filter((notif) => notif.id !== id);
	}
};

const NOTIF_KEY = Symbol('NOTIF');

export function setNotification() {
	return setContext(NOTIF_KEY, new Notifier());
}

export function getNotification(): Notifier {
	return getContext<Notifier>(NOTIF_KEY);
}
