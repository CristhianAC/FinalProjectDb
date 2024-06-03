import React from 'react';

const CartItems = ({ carrito }) => {
  // Ensure carrito is defined and is an array
  const cartItems = carrito || [];

  return (
    <div>
      <div className="flex flex-col justify-center items-center space-y-4">
        {cartItems.length > 0 ? (
          cartItems.map((item, index) => {
            const product = item.product || {};
            return (
              <div key={index} className="flex flex-col justify-center items-center space-y-4 p-4 border rounded-lg shadow-2xl shadow-black/40">
                <div className="w-34 h-28 flex justify-center items-center overflow-hidden">
                  {product.imagen && (
                    <img src={product.imagen} alt={product.nomproducto || 'Product Image'} className="object-contain h-full w-full" />
                  )}
                </div>
                <h4 className="font-bold">{product.nomproducto || 'Nombre del producto'}</h4>
                <p>{product.descrip || 'Descripción del producto'}</p>
                <p>Precio: {product.precio ? `${product.precio} COP` : 'Precio no disponible'}</p>
              </div>
            );
          })
        ) : (
          <p>No hay items en el carrito</p>
        )}
      </div>
    </div>
  );
};

export default CartItems;
