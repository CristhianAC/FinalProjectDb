import React, { useState } from "react";
import { makePetition } from "./API/Conexion-api";
import Autocomplete from "./Servicios/AutoComplete";

const CartItems = ({ carrito, session }) => {
  const cartItems = carrito || [];
  const [address, setAddress] = useState("");

  const makeAPayment = async () => {
    await makePetition(session?.user?.email);
  };

  const handlePlaceSelected = (place) => {
    if (place.formatted_address) {
      setAddress(place.formatted_address);
    }
  };
  const [inputValue, setInputValue] = useState("");
  const [filteredOptions, setFilteredOptions] = useState([
    "+57 300 123 4567",
    "+57 310 234 5678",
    "+57 320 345 6789",
    "+57 301 456 7890",
    "+57 311 567 8901",
  ]);

  const options = [
    "+57 300 123 4567",
    "+57 310 234 5678",
    "+57 320 345 6789",
    "+57 301 456 7890",
    "+57 311 567 8901",
  ];

  const handleInputChange = (e) => {
    const value = e.target.value;
    setInputValue(value);
    setFilteredOptions(
      options.filter((option) =>
        option.toLowerCase().includes(value.toLowerCase())
      )
    );
  };

  return (
    <div className="flex flex-col items-center space-y-20">
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
          <button
            className="btn bg-blue-600 text-white rounded-lg p-2 justify-center items-center"
            onClick={makeAPayment}
          >
            Comprar
          </button>
        </div>
      )}
    </div>
  );
};

export default CartItems;
