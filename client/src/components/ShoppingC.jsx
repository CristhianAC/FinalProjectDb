import { Link } from "react-router-dom";


const ShoppingC = ({ cart }) => {
  
    return (
      <div>
        <button className='back-to-products'>
          <Link to='/productos/' className='back-to-products'>
            <i className="fas fa-arrow-left"></i>
            <span>Productos</span>
          </Link>
        </button>


      </div>
    );
  };
  
export default ShoppingC;