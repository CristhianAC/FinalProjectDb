import React, { useState, useEffect } from 'react';
import Items from './Items';
import SearchBar from './SearchBar';
import PriceFilter from './PriceFilter';
import { getProducts } from './API/Conexion-api';

function App() {
  const [cart, setCart] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(50000); // Ajusta el valor máximo según tus necesidades
  const [showFilter, setShowFilter] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetchProductos();
  }, []);

  const fetchProductos = async () => {
    try {
      const response = await getProducts();
      
      setItems(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const addToCart = (item) => {
    setCart([...cart, item]);
    alert(`${item.name} añadido al carrito`);
  };

  const filteredItems = items.filter(item => 
    item.nomproducto.toLowerCase().includes(searchTerm.toLowerCase()) &&
    item.precio >= minPrice &&
    item.precio <= maxPrice
  );

  return (
    <div className='contenedor max-md:px-0 px-20'>
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
