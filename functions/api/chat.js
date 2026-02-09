export async function onRequest(context) {
  // 1. Get the request body (user message)
  let requestBody;
  try {
    requestBody = await context.request.json();
  } catch (e) {
    return new Response('Invalid JSON', { status: 400 });
  }

  const { message, country, currency } = requestBody;

  // 2. Get API Key from Environment Variable (Securely stored in Cloudflare)
  const apiKey = context.env.GEMINI_API_KEY;

  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'API Key not configured on server' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // 3. Construct the prompt
  const prompt = `당신은 프리랜서 시급 추천 전문가입니다. 
현재 선택된 국가: ${country}
사용자 질문: ${message}

사용자의 업종, 경력, 지역 정보를 바탕으로 적정 시급을 추천해주세요.
추천 시급은 ${currency} 기준으로 제시하고, 간단한 설명을 덧붙여주세요.
답변은 친근하고 간결하게 작성해주세요.`;

  // 4. Call Gemini API
  const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
  
  try {
    const response = await fetch(geminiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
            parts: [{ text: prompt }]
        }],
        generationConfig: {
            temperature: 0.7,
            maxOutputTokens: 500,
        }
      })
    });

    const data = await response.json();
    return new Response(JSON.stringify(data), {
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
