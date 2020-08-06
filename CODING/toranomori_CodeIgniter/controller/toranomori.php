<?php
//|==============================|
//|          INITIALIZE          |
//|==============================|

//[[style()]]
function style() {
	return '
		<style>
			* {
				font-family: Arial, sans-serif;
				color: #333;
				font-size: 12px;
				outline: none;
			}
			/* Anchor */
			a:hover {
				color: #666;
			}
			/* Form */
			form {
				padding: 12px;
				background: #ccffff;
			}
			input, textarea {
				border: none;
				background: #bbeeee;
				margin: 2px;
				padding: 12px;
			}
			input:hover, textarea:hover {
				background: #aadddd;
			}
			input:focus, textarea:focus {
				background: #99cccc;
			}
			textarea {
				width: 404px;
				height: 250px;
			}
		</style>
	';
}

//[[pass()]]
function pass() {
	return 'aaa';
}

//|============|
//|    MAIN    |
//|============|
class Toranomori extends CI_Controller {
	public function chatform() {
		$this->load->database();
		$data['decrypt']  = explode('|', mcrypt_decrypt(MCRYPT_RIJNDAEL_128, pass(), pack('H*', $_GET['token']), MCRYPT_MODE_ECB));
		$data['chatdata'] = $this->db->get_where('Chat', array(
			'thread_id' => $data['decrypt'][0],
			'group_id'  => $data['decrypt'][1]
		))->result_array();
		$data['htmldata'] = '';
		for ($i = 0; $i != count($data['chatdata']); $i++) {
			$data['htmldata'] .= '
				<div class="textbox">
					<span class="text">
						' . htmlspecialchars($data['chatdata'][$i]['text']) . '
						<span class="time">
							' . $data['chatdata'][$i]['time'] . '
						</span>
					</span>
				</div>
			';
		}
		
		$this->load->view('toranomori/chatform', $data);
	}
	public function chat() {
		$this->load->database();
		$data['decrypt'] = explode('|', mcrypt_decrypt(MCRYPT_RIJNDAEL_128, pass(), pack('H*', $_POST['token']), MCRYPT_MODE_ECB));
		$this->db->insert('Chat', array(
			'thread_id' => $data['decrypt'][0],
			'group_id'  => $data['decrypt'][1],
			'time'      => 'Contributed at ' . date(DATE_RFC822) . ' by ' . $_SERVER['REMOTE_ADDR'],
			'text'      => $_POST['text'],
		));
	}
	public function createtoken() {
		echo bin2hex(mcrypt_encrypt(MCRYPT_RIJNDAEL_128, pass(), $_GET['thread_id'] . '|' . $_GET['group_id'] . '|' . mt_rand() . mt_rand(), MCRYPT_MODE_ECB));
	}
}
