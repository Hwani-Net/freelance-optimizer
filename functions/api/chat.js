export async function onRequest(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  };

  // 1. Check Request Method
  if (context.request.method !== "POST") {
    return new Response(JSON.stringify({ error: "Method not allowed" }), { status: 405, headers });
  }

  // 2. Safely Parse Request Body
  let message, country, currency;
  try {
    const requestBody = await context.request.json();
    message = requestBody.message;
    country = requestBody.country || 'Unknown';
    currency = requestBody.currency || 'KRW';
  } catch (e) {
    return new Response(JSON.stringify({ error: "Invalid JSON body", details: e.message }), { status: 400, headers });
  }

  if (!message) {
    return new Response(JSON.stringify({ error: "Message is required" }), { status: 400, headers });
  }

  // 3. API Key Validation (Check multiple possible env var names)
  const apiKey = context.env.GEMINI_API_KEY || context.env.GOOGLE_API_KEY || context.env.API_KEY;
  
  if (!apiKey) {
    console.error("API Key Missing in context.env");
    return new Response(JSON.stringify({ 
      error: "Configuration Error", 
      message: "API Key is missing in Cloudflare environment. Please check Pages Settings > Functions > Environment variables.",
      debug_env_keys: Object.keys(context.env || {})
    }), { status: 500, headers });
  }

  // 4. Construct Prompt
  const prompt = `당신은 프리랜서 시급 추천 전문가 '김비서'입니다. 
  사용자의 지역(${country})과 통화(${currency})를 고려하여 답변하세요.
  사용자 질문: "${message}"
  답변 원칙:
  1. 한국어로 친절하게 답변하세요.
  2. 2026년 기준 인플레이션과 시장 트렌드를 반영하세요.
  3. 구체적인 시급 범위와 그 이유를 전문가답게 조언해주세요.`;

  // 5. Call Gemini API (Try v1beta if v1 fails, but stick to v1 for now)
  const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
  
  try {
    const apiResponse = await fetch(geminiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ role: "user", parts: [{ text: prompt }] }],
        generationConfig: { temperature: 0.7, maxOutputTokens: 1024 }
      })
    });

    const responseText = await apiResponse.text();
    let data;
    try {
        data = JSON.parse(responseText);
    } catch (e) {
        return new Response(JSON.stringify({ 
            error: "Google API non-JSON response", 
            status: apiResponse.status,
            body: responseText.substring(0, 500)
        }), { status: 500, headers });
    }
    
    if (!apiResponse.ok) {
      return new Response(JSON.stringify({ 
        error: "Google AI API Error", 
        message: data.error?.message || "Unknown error from Google",
        details: data 
      }), { status: apiResponse.status, headers });
    }

    return new Response(JSON.stringify(data), { headers });

  } catch (error) {
    return new Response(JSON.stringify({ 
        error: "Worker Exception", 
        message: error.message,
        stack: error.stack
    }), { status: 500, headers });
  }
}
