
const CartItems = ({ cart }) => {
    return (
        <div>
            <div className="flex flex-col justify-center items-center space-y-4">
                {cart.map((item, index) => (
                    <div key={index} className="flex flex-col justify-center items-center space-y-4">
                        <div className=" w-34 h-28 justify-center items-center overflow-hidden shadow-2xl shadow-black/40">
                            <img src={item.image} alt={item.name} className="object-contain" />
                        </div>
                        <h4 className=" font-bold">{item.name}</h4>
                        <p>{item.description}</p>
                        <p>Precio: {item.price} COP</p>
                    </div>
                ))}
            </div>
        </div>
    );
    }