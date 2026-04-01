import { useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!message) return;

    const userMsg = { type: "user", text: message };
    setMessages((prev) => [...prev, userMsg]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message,
      });

      const riskValue = res.data.risk === "High" ? 80 : 30;

      const botMsg = {
        type: "bot",
        text: res.data.reply,
        risk: res.data.risk,
        chart: {
          labels: ["Now", "1hr", "3hr", "6hr"],
          datasets: [
            {
              label: "Risk Trend",
              data: [20, 40, 60, riskValue],
              borderColor: "#22c55e",
              tension: 0.4,
            },
          ],
        },
      };

      setMessages((prev) => [...prev, botMsg]);
      setMessage("");

    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="app">
      <h1>🧠 AI Health Assistant</h1>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={`msg ${msg.type}`}>
            <p>{msg.text}</p>

            {msg.risk && (
              <span className="risk">⚠️ Risk: {msg.risk}</span>
            )}

            {msg.chart && (
              <div style={{ marginTop: "10px" }}>
                <Line data={msg.chart} />
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Describe your symptoms..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;

