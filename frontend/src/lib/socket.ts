import { io } from "socket.io-client";
import env from "$lib/env";

export const socket = io(env.BACKEND_URL);
