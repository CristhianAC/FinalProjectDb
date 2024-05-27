import React, { useState } from 'react';
import Items from './Items';


function App() {
  const [cart, setCart] = useState([]);

  const items = [
    { name: 'Pan de Bono', price: 3000, image: '/src/assets/Pan-de-bonojpg.jpg' },
    { name: 'Pan de Queso', price: 4000, image: '/src/assets/Pan-de-queso.jpg' },
    // Añadir más items según sea necesario
  ];

  const addToCart = (item) => {
    setCart([...cart, item]);
    alert(`${item.name} añadido al carrito`);
  };

  return (
    <div className='container'>
      <Items items={items} addToCart={addToCart} />
    </div>
  );
}

export default App;
