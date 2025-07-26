import React, { createContext, useContext, useState, useEffect } from 'react';

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [conversationId, setConversationId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  // Load conversation history when app starts
  useEffect(() => {
    fetch("http://localhost:8000/api/conversations")
      .then((res) => res.json())
      .then((data) => setHistory(data))
      .catch((err) => console.error("Failed to load conversation history:", err));
  }, []);

  // Send user message and get AI reply
  const handleSend = async (input) => {
    if (!input.trim()) return;

    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: "user123", // You can make this dynamic if needed
          message: input,
          conversation_id: conversationId,
        }),
      });

      const data = await res.json();
      setMessages([...newMessages, { sender: "ai", text: data.ai_response }]);
      setConversationId(data.conversation_id);

      // Reload conversation list
      fetch("http://localhost:8000/api/conversations")
        .then((res) => res.json())
        .then((data) => setHistory(data));
    } catch (error) {
      console.error("Chat error:", error);
      alert("Something went wrong while talking to the chatbot.");
    } finally {
      setLoading(false);
    }
  };

  // Load messages from a specific conversation
  const loadConversation = async (id) => {
    try {
      const res = await fetch(`http://localhost:8000/api/conversations/${id}`);
      const data = await res.json();

      setMessages(
        data.messages.map((m) => ({
          sender: m.sender,
          text: m.text,
        }))
      );
      setConversationId(id);
    } catch (err) {
      console.error("Failed to load conversation:", err);
      alert("Could not load conversation.");
    }
  };

  return (
    <ChatContext.Provider
      value={{
        messages,
        setMessages,
        conversationId,
        setConversationId,
        loading,
        setLoading,
        history,
        setHistory,
        handleSend,
        loadConversation,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => useContext(ChatContext);
