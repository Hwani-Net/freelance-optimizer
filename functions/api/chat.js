export async function onRequest(context) {
  // 1. Check Request Method
  if (context.request.method !== "POST") {
    return new Response(JSON.stringify({ error: "Method not allowed" }), { 
        status: 405,
        headers: { 'Content-Type': 'application/json' }
    });
  }

  // 2. Safely Parse Request Body
  let message, country, currency;
  try {
    const requestBody = await context.request.json();
    message = requestBody.message;
    country = requestBody.country || 'Unknown';
    currency = requestBody.currency || 'KRW';
  } catch (e) {
    return new Response(JSON.stringify({ error: "Invalid JSON body" }), { 
        status: 400,
        headers: { 'Content-Type': 'application/json' }
    });
  }

  if (!message) {
    return new Response(JSON.stringify({ error: "Message is required" }), { 
        status: 400,
        headers: { 'Content-Type': 'application/json' }
    });
  }

  // 3. API Key Validation
  const apiKey = context?.env?.GEMINI_API_KEY || context?.env?.GOOGLE_API_KEY;
  if (!apiKey) {
    return new Response(JSON.stringify({ 
      error: "서버 설정 오류: API Key가 누락되었습니다. Cloudflare 관리자에게 문의하세요.",
      details: "GEMINI_API_KEY or GOOGLE_API_KEY is not set in environment variables."
    }), { 
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // 4. Construct Prompt
  const prompt = `당신은 프리랜서 시급 추천 전문가 '김비서'입니다. 
  사용자의 지역(${country})과 통화(${currency})를 고려하여 답변하세요.
  
  사용자 질문: "${message}"
  
  답변 원칙:
  1. 한국어로 친절하게 답변하세요.
  2. 2026년 기준 인플레이션과 시장 트렌드를 반영하세요.
  3. 구체적인 시급 범위와 그 이유를 전문가답게 조언해주세요.`;

  // 5. Call Gemini API (v1 for stability)
  const geminiUrl = `https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
  
  try {
    const response = await fetch(geminiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ 
            role: "user",
            parts: [{ text: prompt }] 
        }],
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 1024,
        }
      })
    });

    const data = await response.json();
    
    if (!response.ok) {
      return new Response(JSON.stringify({ 
        error: "Google AI API Error", 
        message: data.error?.message || "Unknown error from Google",
        details: data 
      }), { 
        status: response.status,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Success: return the same structure as Google API for frontend compatibility
    return new Response(JSON.stringify(data), {
      headers: { 
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*' 
      }
    });

  } catch (error) {
    return new Response(JSON.stringify({ 
        error: "Internal Server Error", 
        message: error.message 
    }), { 
        status: 500,
        headers: { 'Content-Type': 'application/json' }
    });
  }
}
