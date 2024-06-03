import React, { useState, useEffect } from "react";
import Items from "./Items";
import SearchBar from "./SearchBar";
import PriceFilter from "./PriceFilter";
import { getProducts, addCarrito, getCarrito } from "./API/Conexion-api";
import { Link } from "react-router-dom";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function ItemManager({ session }) {
  const [cart, setCart] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(50000);
  const [showFilter, setShowFilter] = useState(false);
  const [items, setItems] = useState([]);
  const [quantity, setQuantity] = useState(0);

  useEffect(() => {
    loadData();
  }, []);

  useEffect(() => {
    setQuantity(cart.reduce((acc, [, value]) => acc + value, 0));
    if (cart.length > 0) {
      addCarrito(session.user.email, cart)
        .then(response => {
          console.log("Carrito actualizado:", response);
        })
        .catch(error => {
          console.error("Error al actualizar el carrito:", error);
        });
    }
  }, [cart]);

  const loadData = async () => {
    try {
      const [productsResponse, cartResponse] = await Promise.all([
        getProducts(),
        getCarrito(session.user.email),
      ]);
  
      const products = productsResponse.data;
      const cartItems = cartResponse.productos;
  
      const itemsWithQuantity = products.map((product) => {
        const cartItem = cartItems.find((item) => item.producto === product.idp);
        return {
          ...product,
          cantidad: cartItem ? cartItem.cantidad : 0,
        };
      });
  
      setItems(itemsWithQuantity);
  
      const initialCart = cartItems.map((item) => {
        const product = products.find(p => p.idp === item.producto);
        return [product.nomproducto, item.cantidad, product];
      });
      setCart(initialCart);
    } catch (error) {
      console.error("Error al cargar los datos:", error);
    }
  };
  

  const addToCart = (item) => {
    const existingItemIndex = cart.findIndex((cartItem) => cartItem[0] === item[0]);

    if (existingItemIndex !== -1) {
      let newCart = cart.map((cartItem, index) =>
        index === existingItemIndex ? [cartItem[0], item[1], item[2]] : cartItem
      );
      newCart = newCart.filter((i) => i[1] !== 0);

      if (newCart.length === 0) {
        setCart([]);
        toast("No hay elementos en el carrito con cantidad distinta de cero");
      } else {
        setCart(newCart);
      }
    } else {
      setCart([...cart, item]);
      toast(`${item[0]} añadido al carrito`);
    }
  };

  const filteredItems = items.filter(
    (item) =>
      item.nomproducto.toLowerCase().includes(searchTerm.toLowerCase()) &&
      item.precio >= minPrice &&
      item.precio <= maxPrice
  );

  return (
    <div className="contenedor max-md:px-0 px-20 bg-[#b9825f] p-10">
      <ToastContainer position="bottom-right" />
      <button className="open-shopiing-cart">
        <Link to="/ShoppingC" className="ShoppingCart space-x-2">
          <i className="fas fa-shopping-cart"></i>
          <span>{quantity}</span>
        </Link>
      </button>

      <button
        className="open-filter-button"
        onClick={() => setShowFilter(!showFilter)}
      >
        <i className="fas fa-search"></i>
      </button>

      {showFilter && (
        <nav className="filter-nav">
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

export default ItemManager;
