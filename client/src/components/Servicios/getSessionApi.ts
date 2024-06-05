import { SessionType, usuario } from "../API/sessionType";
import { validateClient } from "../API/Conexion-api";
async function iniciarSession(
  emailt: string,
  password: string
): Promise<SessionType | null> {
  try {
    const response = await validateClient(emailt, password);
    let user = null;

    const { email, name, idc} = response.data;
    if (response.data) {
      window.localStorage.setItem("email", email);
      window.localStorage.setItem("name", name);
      window.localStorage.setItem("id", idc);
      user = new usuario(email, name, idc);
      return new SessionType(user);
    }

    return null;
  } catch (error) {
    console.error("Error fetching user data:", error);
    return null;
  }
}

async function tomarSesion(): Promise<SessionType | null> {
    const email = window.localStorage.getItem("email");
    const name = window.localStorage.getItem("name");
    const id = window.localStorage.getItem("idc");
    
    if (email && name && id) {
        const user = new usuario(email, name, id);
        return new SessionType(user);
    }
    
    return null;
    
}
async function cerrarSesion() {
  window.localStorage.removeItem("email");
  window.localStorage.removeItem("name");
  window.localStorage.removeItem("id");
}
