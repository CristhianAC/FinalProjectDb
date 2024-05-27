import React, { useState } from 'react';
import Items from './Items';
import SearchBar from './SearchBar';
import PriceFilter from './PriceFilter';

function App() {
  const [cart, setCart] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(50000); // Ajusta el valor máximo según tus necesidades
  const [showFilter, setShowFilter] = useState(false);

  const items = [
    { name: 'Pan de Bono', price: 3000, image: '/src/assets/Pan-de-bonojpg.jpg' },
    { name: 'Pan de Queso', price: 4000, image: '/src/assets/Pan-de-queso.jpg' },
    { name: 'Pizza Perro', price: 35000, image: '/src/assets/pizza_perro.png'},
    { name: 'Pan de Yuca', price: 5000, image: '/src/assets/pan-de-yuca.jpg'},
    { name: 'Pan de Molde', price: 5000, image: '/src/assets/pan-de-molde.jpg'},
    // Añadir más items según sea necesario
  ];

  const addToCart = (item) => {
    setCart([...cart, item]);
    alert(`${item.name} añadido al carrito`);
  };

  const filteredItems = items.filter(item => 
    item.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
    item.price >= minPrice &&
    item.price <= maxPrice
  );

  return (
    <div className='contenedor'>
      <button 
        className='open-filter-button'
        onClick={() => setShowFilter(!showFilter)}
      >
        <i className="fas fa-search"></i>
      </button>
      
      {showFilter && (
        <nav className='filter-nav'>
          <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
          <PriceFilter 
            minPrice={minPrice} 
            maxPrice={maxPrice} 
            setMinPrice={setMinPrice} 
            setMaxPrice={setMaxPrice}
          />
        </nav>
      )}
      
      <Items items={filteredItems} addToCart={addToCart} />
    </div>
  );
}

export default App;