import { Link } from "react-router-dom";
import CartItems from "./CartItems";
import { useEffect, useState } from "react";
import { getCarrito, getProductDetails } from "./API/Conexion-api";

const ShoppingC = ({ session }) => {
  const [shoppingCart, setShoppingCart] = useState([]);

  useEffect(() => {
    const fetchCart = async () => {
      if (session && session.user.email) {
        try {
          const cartData = await getCarrito(session.user.email);
          console.log(cartData);
          const productDetails = await Promise.all(
            cartData.productos.map(async (item) => {
              const response = await getProductDetails(item.producto);
              console.log(response);
              const product = response.data;
              return { ...item, product };
            })
          );
          setShoppingCart(productDetails);
        } catch (error) {
          console.error('Error fetching cart:', error);
        }
      }
    };
    fetchCart();
  }, [session]);

  return (
    <section className="shopping-cart-container p-10 bg-gray-100 min-h-screen">
      <div className="flex justify-between items-center mb-6">
        <button className="bg-[#f7f3e9] text-[#310e11] p-3 hover:bg-[#aca9a3] transition-all duration-500 rounded-2xl">
          <Link to="/productos/" className="flex items-center">
            <i className="fas fa-arrow-left mr-2"></i>
            <span>Productos</span>
          </Link>
        </button>
        <h2 className="text-2xl font-bold">Carrito</h2>
      </div>
      <div>
        <CartItems carrito={shoppingCart} session={session}/>
      </div>
      
    </section>
  );
};

export default ShoppingC;
