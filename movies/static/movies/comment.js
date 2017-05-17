function showFormComment(id){
	$('#parent').val(id);
	//$('#commentModal').modal('show');
	$('#commentModal').on('show.bs.modal', function(){
		$('#comment_text').focus();
	})
}