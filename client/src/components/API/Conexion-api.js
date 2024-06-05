import axios from "axios";

export const getProducts = () =>
  axios.get(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/producto/"
  );

export const getClienteGoogle = (email, nombre) =>
  axios.post(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/cliente/google_login/",
    {
      correo: email,
      nombre: nombre,
    }
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
      cantidad: cantidad,
    }
  );

export const addCarrito = async (correo, Carrito) => {
  try {
    const promises = Carrito.map((element) => {
      console.log("Adding item:", {
        correo: correo,
        producto_id: element[2].idp,
        cantidad: element[1],
      });
      return agregarItem(correo, element[2].idp, element[1]);
    });
    await Promise.all(promises);
  } catch (error) {
    console.error("Error al agregar al carrito:", error);
    throw error;
  }
};

export const getCarrito = async (correo) => {
  const response = await axios.get(
    `https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/carritoproducto/get_cart/?correo=${correo}`
  );
  return response.data;
};

export const getProductDetails = (idp) =>
  axios.get(
    `https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/producto/pedirProducto/?idp=${idp}`
  );

export const makePetition = (correo, numero, direccion, pickup, comentario) =>
  axios.post(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/pedido/agregar_pedido/",
    {
      correo: correo,
      numero: numero,
      direccion: direccion,
      pickup: pickup,
      comentario: comentario,
    }
  );

export const getNumeros = async (correo) => {
  const response = await axios.get(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/telefono/get_telefono/?correo=" +
      correo
  );
  return response.data;
};
export const postNumeros = (correo) =>
  axios.post(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/telefono/agregar_telefono/",
    {
      correo: correo,
      
    }
  );
export const getDomiciliarios = (email) =>
  axios.get(
    "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/repartidor/verif_repartidor/?correo=" + email
  );
  export const getPedido= (email) =>
    axios.get(
      "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/repartidor/get_pedido/?correo=" + email
    );

  export const activar = (email) =>
    axios.put(
      "https://quillas-bakery-cristhianac-5656dd75.koyeb.app/api/repartidor/activar_repartidor/",{
        correo: email
      }
    );