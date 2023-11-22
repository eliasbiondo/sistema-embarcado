'use client'
// Importing necessary hooks and components from React and Next.js
import { useState, useEffect, useCallback } from 'react';
import Image from 'next/image';
import mqtt from 'mqtt';

// Importing SVG images
import BulbOff from '../public/bulb-0.svg';
import BulbOn from '../public/bulb-1.svg';

/**
 * Custom hook to manage MQTT connection and messages
 * @returns {Object} An object containing the read value from MQTT and a function to disconnect the client
 */
function useMQTTClient() {
  const [readValue, setReadValue] = useState(0);
  const client = mqtt.connect('ws://test.mosquitto.org:8080');

  useEffect(() => {
    // Subscribe to the MQTT topic on connection
    client.on('connect', () => {
      client.subscribe('sensor/ldr/a8eee424575c6c51bc07d9bd7d8f1277', (err) => {
        if (err) {
          console.error('Connection error:', err);
        } else {
          console.log('Connected to the MQTT broker');
        }
      });
    });

    // Handle incoming messages
    client.on('message', (topic, message) => {
      if (topic === 'sensor/ldr/a8eee424575c6c51bc07d9bd7d8f1277') {
        const value = Number(message.toString());
        setReadValue(value);
      }
    });
  }, [client]);

  // Expose the read value and a disconnect function
  return { readValue, disconnect: () => client.end() };
}

/**
 * Home component displaying the MQTT sensor data and corresponding bulb images
 * @returns {JSX.Element} The Home component
 */
export default function Home() {
  // State for each bulb's on/off status
  const [firstBulb, setFirstBulb] = useState(false);
  const [secondBulb, setSecondBulb] = useState(false);
  const [thirdBulb, setThirdBulb] = useState(false);

  // Use the custom hook to manage MQTT connection and messages
  const { readValue } = useMQTTClient();

  // Update bulb states based on the read value
  useEffect(() => {
    setFirstBulb(readValue >= 6000);
    setSecondBulb(readValue >= 25000);
    setThirdBulb(readValue >= 55000);
  }, [readValue]);

  return (
    <main className="flex flex-col gap-16 px-32 py-24">
      <header className='flex flex-col gap-4'>
        <h1 className='text-4xl font-bold'>Sistema embarcado</h1>
        <h2 className='text-xl'>Leitura de fotorresistência</h2>
      </header>
      <section className="flex gap-8">
        {/* Display bulb images based on their state */}
        <Image src={firstBulb ? BulbOn : BulbOff} alt="Lâmpada 1" />
        <Image src={secondBulb ? BulbOn : BulbOff} alt="Lâmpada 2" />
        <Image src={thirdBulb ? BulbOn : BulbOff} alt="Lâmpada 3" />
      </section>
      <section className="flex flex-col">
        <p className="text-xl font-bold">Valor lido</p>
        <p className='text-xl'>{readValue}</p>
      </section>
    </main>
  );
}
