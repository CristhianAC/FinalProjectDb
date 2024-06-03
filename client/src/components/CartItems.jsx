import React from 'react';

const CartItems = ({ carrito }) => {
  const cartItems = carrito || [];

  return (
    <div className="flex flex-col items-center space-y-4">
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
                    alt={product.nomproducto || 'Imagen del producto'}
                    className="object-contain h-full w-full"
                  />
                )}
              </div>
              <div className="flex flex-col space-y-2 flex-grow">
                <h4 className="font-bold text-lg text-gray-600">{product.nomproducto || 'Nombre del producto'}</h4>
                <p className="text-gray-600">{product.descrip || 'Descripción del producto'}</p>
                <p className="text-green-600 font-semibold">Total: {product.precio ? `${product.precio * item.cantidad} COP` : 'Precio no disponible'}</p>
                <p className="text-blue-600">Cantidad: {item.cantidad}</p>
              </div>
            </div>
          );
        })
      ) : (
        <p className="text-red-600 font-semibold">No hay items en el carrito</p>
      )}
    </div>
  );
};

export default CartItems;
