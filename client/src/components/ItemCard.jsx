

const ItemCard = ({ image, name, price, description, addToCart }) => {
    return (
        <div className='producto animate-slide-in-bottom flex-col justify-around items-center shadow-2xl shadow-black/40 space-y-4'>
                <div className=" w-34 h-28 justify-center items-center overflow-hidden shadow-2xl shadow-black/40">
                    <img src={image} alt={name} className="object-contain" />
                </div>
                <h4 className=" font-bold">{name}</h4>
                <p>{description}</p>
                <p>Precio: {price} COP</p>
                <button onClick={addToCart} className="btn animate-slide-in-bottom transition-all duration-300 hover:rounded-2xl">Añadir al Carrito</button>
        </div>
    );
};

export default ItemCard;
