
import { useState, useEffect } from "react";
const ItemCard = ({ image, name, price, description, addToCart, item }) => {
  const [value, setValue] = useState(0);
  const [cartAdded, setCartAdded] = useState(false);
  function sumvalue() {
    setValue(value + 1);
  }
  function subvalue() {
    if (value > 0) {
      setValue(value - 1);
    }
    
  }
  useEffect(() => {
    if(cartAdded === true){
    addToCart([item.nomproducto, value]);
     if (value === 0) 
        setCartAdded(false);
    }
    
  }, [value]);
  return (
    <div className="producto animate-slide-in-bottom flex-col justify-around items-center shadow-2xl shadow-black/40 space-y-4">
      <div className=" w-34 h-28 justify-center items-center overflow-hidden shadow-2xl shadow-black/40">
        <img src={image} alt={name} className="object-contain" />
      </div>
      <h4 className=" font-bold">{name}</h4>
      <p>{description}</p>
      <p>Precio: {price} COP</p>
      { cartAdded === true &&<div className="flex flex-row justify-around items-center">
        <button
          onClick={subvalue}
          className="btn animate-slide-in-bottom transition-all duration-300 hover:rounded-2xl"
        >
          -
        </button>
        {value && <p>{value}</p>}
        <button
          onClick={sumvalue}
          className="btn animate-slide-in-bottom transition-all duration-300 hover:rounded-2xl"
        >
          +
        </button>
        
      </div>}
      {!cartAdded&&<button
          onClick={()=>{setCartAdded(true); sumvalue()}}
          className="btn animate-slide-in-bottom transition-all duration-300 hover:rounded-2xl"
        >
          Añadir al Carrito
        </button>}
      
    </div>
  );
};

export default ItemCard;
