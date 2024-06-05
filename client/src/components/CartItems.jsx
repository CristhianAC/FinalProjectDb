import React, { useState, useEffect } from "react";
import { makePetition, getNumeros } from "./API/Conexion-api";
import Autocomplete from "./Servicios/AutoComplete";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Link } from "react-router-dom";

const CartItems = ({ carrito, session }) => {
  const cartItems = carrito || [];
  const [address, setAddress] = useState("");
  const [inputValue, setInputValue] = useState("");
  const [filteredOptions, setFilteredOptions] = useState([]);
  const [phoneOptions, setPhoneOptions] = useState([]);
  const [checked, setChecked] = useState(false);
  const [comments, setComments] = useState("");

  useEffect(() => {
    const fetchPhoneNumbers = async () => {
      if (session?.user?.email) {
        try {
          const phoneNumbers = await getNumeros(session.user.email);
          setPhoneOptions(phoneNumbers.map((phone) => phone.numero));
        } catch (error) {
          console.error("Error fetching phone numbers:", error);
        }
      }
    };
    fetchPhoneNumbers();
  }, [session]);
  useEffect(()=>
  {
    console.log(checked)
  },[checked])
  const handlePlaceSelected = (place) => {
    if (place.formatted_address) {
      setAddress(place.formatted_address);
    }
  };

  const handleInputChange = (e) => {
    const value = e.target.value;
    setInputValue(value);
    setFilteredOptions(
      phoneOptions.filter((option) =>
        option.toLowerCase().includes(value.toLowerCase())
      )
    );
  };

  const handleCommentsChange = (e) => {
    setComments(e.target.value);
  };

  const makeAPayment = async () => {
    console.log(checked)
    await makePetition(
      session?.user?.email,
      inputValue,
      address,
      checked,
      comments
    );
    toast.success("Pedido realizado con éxito");
  };

  return (
    <div className="flex flex-col items-center space-y-20">
      <ToastContainer position="bottom-right" />
      {cartItems.length > 0 ? (
        cartItems.map((item, index) => {
          const product = item.product || {};
          return (
            <div
              key={index}
              className="flex items-center space-x-4 p-4 border rounded-lg shadow-2xl shadow-black/40 w-full max-w-md bg-white"
            >
              <div className="w-32 h-32 flex justify-center items-center overflow-hidden rounded-lg">
                {product.imagen && (
                  <img
                    src={product.imagen}
                    alt={product.nomproducto || "Imagen del producto"}
                    className="object-contain h-full w-full"
                  />
                )}
              </div>
              <div className="flex flex-col space-y-2 flex-grow">
                <h4 className="font-bold text-lg text-gray-600">
                  {product.nomproducto || "Nombre del producto"}
                </h4>
                <p className="text-gray-600">
                  {product.descrip || "Descripción del producto"}
                </p>
                <p className="text-green-600 font-semibold">
                  Total:{" "}
                  {product.precio
                    ? `${product.precio * item.cantidad} COP`
                    : "Precio no disponible"}
                </p>
                <p className="text-blue-600">Cantidad: {item.cantidad}</p>
              </div>
            </div>
          );
        })
      ) : (
        <p className="text-red-600 font-semibold">
          No hay productos en el carrito
        </p>
      )}
      {cartItems.length > 0 && (
        <section className="flex flex-col items-center space-y-20">
          <textarea
            type="text"
            name="comments"
            onChange={handleCommentsChange}
            value={comments}
            placeholder="Comentarios"
            className="border rounded-lg p-2 w-96 h-24 text-start text-black"
          />
          <div className="flex flex-row items-center justify-center space-x-11">
            <Autocomplete onPlaceSelected={handlePlaceSelected} />

            <div className="flex items-center justify-center">
              <input
                list="phone-options"
                value={inputValue}
                onChange={handleInputChange}
                className="border rounded-lg p-2 text-black"
                type="text"
                placeholder="Teléfono"
              />
              <datalist id="phone-options">
                {filteredOptions.map((option, index) => (
                  <option key={index} value={option} />
                ))}
              </datalist>
            </div>

            <div className="flex items-center space-x-2">
              <input
                type="checkbox"
                id="pickup"
                checked={checked}
                onChange={() => setChecked(!checked)}
                className="h-6 w-6 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2 focus:outline-none"
              />
              <label htmlFor="pickup" className="text-gray-700 font-medium">
                Recoger en tienda
              </label>
            </div>

            <Link to="/productos">
              <button
                className="btn bg-blue-600 text-white rounded-lg p-2 justify-center items-center"
                onClick={makeAPayment}
              >
                Comprar
              </button>
            </Link>
          </div>
        </section>
      )}
    </div>
  );
};

export default CartItems;
