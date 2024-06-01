import React from 'react';

const CartItems = ({ carrito }) => {
  // Ensure carrito is defined and is an array
  const cartItems = carrito || [];

  return (
    <div>
      <div className="flex flex-col justify-center items-center space-y-4">
        {cartItems.length > 0 ? (
          cartItems.map((item, index) => (
            <div key={index} className="flex flex-col justify-center items-center space-y-4">
              <div className="w-34 h-28 justify-center items-center overflow-hidden shadow-2xl shadow-black/40">
                <img src={item[2].imagen} alt={item[2].name} className="object-contain" />
              </div>
              <h4 className="font-bold">{item[2].nomProduct}</h4>
              <p>{item[2].description}</p>
              <p>Precio: {item[2].price} COP</p>
            </div>
          ))
        ) : (
          <p>No hay items en el carrito</p>
        )}
      </div>
    </div>
  );
};

export default CartItems;
