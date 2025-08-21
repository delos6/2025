import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function EmojiQuote() {
  const [emoji, setEmoji] = useState("✨");
  const [isAnimating, setIsAnimating] = useState(false);

  const emojis = ["🌸", "💡", "🌈", "🔥", "🌍", "🌟"];

  const handleClick = () => {
    if (isAnimating) return; // 애니메이션 중에는 클릭 방지
    setIsAnimating(true);
    const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
    setEmoji(randomEmoji);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-r from-pink-200 to-blue-200">
      <div className="text-2xl font-bold mb-6">✨ Inspiring Emoji Quote ✨</div>
      <button
        onClick={handleClick}
        className="px-6 py-3 bg-white rounded-2xl shadow-md hover:shadow-xl transition font-semibold"
      >
        Show Emoji
      </button>

      <AnimatePresence>
        {isAnimating && (
          <motion.div
            key={emoji}
            initial={{ opacity: 1, y: 0, scale: 1 }}
            animate={{ opacity: 0, y: -100, scale: 1.5 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 1 }}
            onAnimationComplete={() => setIsAnimating(false)}
            className="text-6xl mt-10"
          >
            {emoji}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
