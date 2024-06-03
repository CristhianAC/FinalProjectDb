import axios from "axios";

export const getProducts = () =>
  axios.get(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/producto/"
  );
export const getClienteGoogle = (email, nombre) =>
  axios.post(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/cliente/google_login/",
    { correo: email, nombre: nombre }
  );

export const addCliente = (email, password, nombre) =>
  axios.post(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/cliente/agregar_cliente/",
    {
      correo: email,
      password: password,
      nombre: nombre,
    }
  );
export const validateClient = (email, password) =>
  axios.get(
    `https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/cliente/check_password/?email=${email}&password=${password}`
  );

export const agregarItem = (correo, idItem, cantidad) =>
  axios.post(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/carritoproducto/add_item/",
    {
        correo: correo,
        producto_id: idItem,
        cantidad: cantidad
    }
  );

export const addCarrito = (correo,Carrito) => {
    Carrito.forEach(element => {
        agregarItem(correo, element[2].idp, element[1]);
    });
}

export const getCarrito = (correo) => 
  axios.get(
    `https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/carritoproducto/get_carrito/?correo=${correo}`
  );