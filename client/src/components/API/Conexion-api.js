import axios from "axios";

export const getProducts = () => axios.get("https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/producto/");
export const getClienteGoogle = (email) => axios.get("https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/cliente/check_cliente/", {params: {correo: email}});
export const addCliente =  (email, password, nombre, apellido) => axios.post("https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/cliente/agregar_cliente", {params: {correo: email, password: password, nombre: nombre, apellido: apellido}});

