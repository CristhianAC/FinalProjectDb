import React, { useState } from 'react';
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

  let items;

  const fetchProductos = async () => {
    try {
      const response = await getProducts();
      console.log(response.data);
      items = response.data;
    } catch (error) {
      console.error(error);
    }
  };



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
      
      <Items {console.log(items)} items={filteredItems} addToCart={addToCart} />
    </div>
  );
}

export default App;