import { getDomiciliarios, getPedido } from "./API/Conexion-api";
import React, { useEffect, useState } from "react";

function Domicilio({ session }) {
  const [correct, setCorrect] = useState(null);
  const [domicilio, setDomicilio] = useState(null);
  useEffect(() => {
    const fetchDomiciliarios = async () => {
      try {
        const domiciliarios = await getDomiciliarios(session.user.email);
        setCorrect(domiciliarios);
      } catch (error) {
        console.error("Error fetching domiciliarios:", error);
      }
    };
    fetchDomiciliarios();
  }, []);
  async function handleDomicilio() {
    if (correct.activo == true) {
      const pedido = await getPedido(session.user.email);
      setDomicilio(pedido);
    }
  }
  return (
    <section>
      {correct ? (
        <section>
          <h1>
            ¡Hola! {session.user.email} eres un repartidor activo, puedes
            revisar tus pedidos
          </h1>
          <button onClick={handleDomicilio}>Ver pedidos</button>
          {domicilio ? (
            <section>
              <h2>Pedidos</h2>
              {domicilio.map((pedido, index) => {
                return (
                  <section key={index}>
                    <h3>Pedido {index + 1}</h3>
                    <p>Correo: {pedido.correo}</p>
                    <p>Numero: {pedido.numero}</p>
                    <p>Direccion: {pedido.direccion}</p>
                  </section>
                );
              })}
            </section>
          ) : null}
        </section>
      ) : (
        <h1>
          ¡Hola! recuerda que este es un sitio solo para repartidores, inicia
          session con una cuenta de repartidor
        </h1>
      )}
    </section>
  );
}

export default Domicilio;
