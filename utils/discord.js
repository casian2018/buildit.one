import axios from 'axios';

const webhookUrl = 'https://discord.com/api/webhooks/1234518756999565402/nG_DG-Jd6rM1El3N1sdqYJTNreqbB_vvUiGBjRHOrvzokVhSnKYFUqXcBWG1fWQKL-ua';

export const sendAuthCodeToDiscord = async (code) => {
  try {
    await axios.post(webhookUrl, {
      content: `Your authentication code for buildit.one is: ${code} `
    });
  } catch (error) {
    console.error('Error sending Discord webhook:', error);
  }
};
