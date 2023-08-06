cdef extern from "mpack-src/src/mpack.c":

    ctypedef int mpack_sint32_t

    ctypedef unsigned int mpack_uint32_t

    cdef struct mpack_value_s:
        mpack_uint32_t lo
        mpack_uint32_t hi

    ctypedef mpack_value_s mpack_value_t

    cdef enum:
        MPACK_OK
        MPACK_EOF
        MPACK_ERROR

    cdef enum _mpack_token_type_t_e:
        MPACK_TOKEN_NIL
        MPACK_TOKEN_BOOLEAN
        MPACK_TOKEN_UINT
        MPACK_TOKEN_SINT
        MPACK_TOKEN_FLOAT
        MPACK_TOKEN_CHUNK
        MPACK_TOKEN_ARRAY
        MPACK_TOKEN_MAP
        MPACK_TOKEN_BIN
        MPACK_TOKEN_STR
        MPACK_TOKEN_EXT

    ctypedef _mpack_token_type_t_e mpack_token_type_t

    cdef union _mpack_token_t_mpack_token_t_mpack_token_s_data_u:
        mpack_value_t value
        char* chunk_ptr
        int ext_type

    cdef struct mpack_token_s:
        mpack_token_type_t type
        mpack_uint32_t length
        _mpack_token_t_mpack_token_t_mpack_token_s_data_u data

    ctypedef mpack_token_s mpack_token_t

    cdef struct mpack_tokbuf_s:
        char pending[1]
        mpack_token_t pending_tok
        size_t ppos
        size_t plen
        mpack_uint32_t passthrough

    ctypedef mpack_tokbuf_s mpack_tokbuf_t

    void mpack_tokbuf_init(mpack_tokbuf_t* tb)

    int mpack_read(mpack_tokbuf_t* tb, char** b, size_t* bl, mpack_token_t* tok)

    int mpack_write(mpack_tokbuf_t* tb, char** b, size_t* bl, mpack_token_t* tok)

    int mpack_rtoken(char** buf, size_t* buflen, mpack_token_t* tok)

    int mpack_rpending(char** b, size_t* nl, mpack_tokbuf_t* tb)

    int mpack_rvalue(mpack_token_type_t t, mpack_uint32_t l, char** b, size_t* bl, mpack_token_t* tok)

    int mpack_rblob(mpack_token_type_t t, mpack_uint32_t l, char** b, size_t* bl, mpack_token_t* tok)

    int mpack_wtoken(mpack_token_t* tok, char** b, size_t* bl)

    int mpack_wpending(char** b, size_t* bl, mpack_tokbuf_t* tb)

    int mpack_wpint(char** b, size_t* bl, mpack_value_t v)

    int mpack_wnint(char** b, size_t* bl, mpack_value_t v)

    int mpack_wfloat(char** b, size_t* bl, mpack_token_t* v)

    int mpack_wstr(char** buf, size_t* buflen, mpack_uint32_t len)

    int mpack_wbin(char** buf, size_t* buflen, mpack_uint32_t len)

    int mpack_wext(char** buf, size_t* buflen, int type, mpack_uint32_t len)

    int mpack_warray(char** buf, size_t* buflen, mpack_uint32_t len)

    int mpack_wmap(char** buf, size_t* buflen, mpack_uint32_t len)

    int mpack_w1(char** b, size_t* bl, mpack_uint32_t v)

    int mpack_w2(char** b, size_t* bl, mpack_uint32_t v)

    int mpack_w4(char** b, size_t* bl, mpack_uint32_t v)

    mpack_value_t mpack_byte(unsigned char b)

    int mpack_value(mpack_token_type_t t, mpack_uint32_t l, mpack_value_t v, mpack_token_t* tok)

    int mpack_blob(mpack_token_type_t t, mpack_uint32_t l, int et, mpack_token_t* tok)

    ctypedef mpack_sint32_t mpack_sintmax_t

    ctypedef mpack_uint32_t mpack_uintmax_t

    mpack_token_t mpack_pack_nil()

    mpack_token_t mpack_pack_boolean(unsigned v)

    mpack_token_t mpack_pack_uint(mpack_uintmax_t v)

    mpack_token_t mpack_pack_sint(mpack_sintmax_t v)

    mpack_token_t mpack_pack_float_compat(double v)

    mpack_token_t mpack_pack_float_fast(double v)

    mpack_token_t mpack_pack_number(double v)

    mpack_token_t mpack_pack_chunk(char* p, mpack_uint32_t l)

    mpack_token_t mpack_pack_str(mpack_uint32_t l)

    mpack_token_t mpack_pack_bin(mpack_uint32_t l)

    mpack_token_t mpack_pack_ext(int type, mpack_uint32_t l)

    mpack_token_t mpack_pack_array(mpack_uint32_t l)

    mpack_token_t mpack_pack_map(mpack_uint32_t l)

    unsigned mpack_unpack_boolean(mpack_token_t t)

    mpack_uintmax_t mpack_unpack_uint(mpack_token_t t)

    mpack_sintmax_t mpack_unpack_sint(mpack_token_t t)

    double mpack_unpack_float_fast(mpack_token_t t)

    double mpack_unpack_float_compat(mpack_token_t t)

    double mpack_unpack_number(mpack_token_t t)

    int mpack_fits_single(double v)

    mpack_value_t mpack_pack_ieee754(double v, unsigned m, unsigned e)

    int mpack_is_be()

    double mpack_fmod_pow2_32(double a)

    cdef enum:
        MPACK_EXCEPTION
        MPACK_NOMEM

    cdef union _mpack_data_t_u:
        void* p
        mpack_uintmax_t u
        mpack_sintmax_t i
        double d

    ctypedef _mpack_data_t_u mpack_data_t

    cdef struct mpack_node_s:
        mpack_token_t tok
        size_t pos
        int key_visited
        mpack_data_t data[1]

    ctypedef mpack_node_s mpack_node_t

    cdef struct _mpack_one_parser_t_s:
        mpack_data_t data
        mpack_uint32_t size
        mpack_uint32_t capacity
        int status
        int exiting
        mpack_tokbuf_t tokbuf
        mpack_node_t items[1]

    ctypedef _mpack_one_parser_t_s mpack_one_parser_t

    cdef struct _mpack_parser_t_s:
        mpack_data_t data
        mpack_uint32_t size
        mpack_uint32_t capacity
        int status
        int exiting
        mpack_tokbuf_t tokbuf
        mpack_node_t items[1]

    ctypedef _mpack_parser_t_s mpack_parser_t

    ctypedef void (*mpack_walk_cb)(mpack_parser_t* w, mpack_node_t* n)

    void mpack_parser_init(mpack_parser_t* p, mpack_uint32_t c)

    int mpack_parse_tok(mpack_parser_t* walker, mpack_token_t tok, mpack_walk_cb enter_cb, mpack_walk_cb exit_cb)

    int mpack_unparse_tok(mpack_parser_t* walker, mpack_token_t* tok, mpack_walk_cb enter_cb, mpack_walk_cb exit_cb)

    int mpack_parse(mpack_parser_t* parser, char** b, size_t* bl, mpack_walk_cb enter_cb, mpack_walk_cb exit_cb)

    int mpack_unparse(mpack_parser_t* parser, char** b, size_t* bl, mpack_walk_cb enter_cb, mpack_walk_cb exit_cb)

    void mpack_parser_copy(mpack_parser_t* d, mpack_parser_t* s)

    int mpack_parser_full(mpack_parser_t* w)

    mpack_node_t* mpack_parser_push(mpack_parser_t* w)

    mpack_node_t* mpack_parser_pop(mpack_parser_t* w)

    cdef enum:
        MPACK_RPC_REQUEST
        MPACK_RPC_RESPONSE
        MPACK_RPC_NOTIFICATION
        MPACK_RPC_ERROR

    cdef enum:
        MPACK_RPC_EARRAY
        MPACK_RPC_EARRAYL
        MPACK_RPC_ETYPE
        MPACK_RPC_EMSGID
        MPACK_RPC_ERESPID

    cdef struct mpack_rpc_header_s:
        mpack_token_t toks[1]
        int index

    ctypedef mpack_rpc_header_s mpack_rpc_header_t

    cdef struct mpack_rpc_message_s:
        mpack_uint32_t id
        mpack_data_t data

    ctypedef mpack_rpc_message_s mpack_rpc_message_t

    cdef struct mpack_rpc_slot_s:
        int used
        mpack_rpc_message_t msg

    cdef struct _mpack_rpc_one_session_t_s:
        mpack_tokbuf_t reader
        mpack_tokbuf_t writer
        mpack_rpc_header_t receive
        mpack_rpc_header_t send
        mpack_uint32_t request_id
        mpack_uint32_t capacity
        mpack_rpc_slot_s slots[1]

    ctypedef _mpack_rpc_one_session_t_s mpack_rpc_one_session_t

    cdef struct _mpack_rpc_session_t_s:
        mpack_tokbuf_t reader
        mpack_tokbuf_t writer
        mpack_rpc_header_t receive
        mpack_rpc_header_t send
        mpack_uint32_t request_id
        mpack_uint32_t capacity
        mpack_rpc_slot_s slots[1]

    ctypedef _mpack_rpc_session_t_s mpack_rpc_session_t

    void mpack_rpc_session_init(mpack_rpc_session_t* s, mpack_uint32_t c)

    int mpack_rpc_receive_tok(mpack_rpc_session_t* s, mpack_token_t t, mpack_rpc_message_t* msg)

    int mpack_rpc_request_tok(mpack_rpc_session_t* s, mpack_token_t* t, mpack_data_t d)

    int mpack_rpc_reply_tok(mpack_rpc_session_t* s, mpack_token_t* t, mpack_uint32_t i)

    int mpack_rpc_notify_tok(mpack_rpc_session_t* s, mpack_token_t* t)

    int mpack_rpc_receive(mpack_rpc_session_t* s, char** b, size_t* bl, mpack_rpc_message_t* m)

    int mpack_rpc_request(mpack_rpc_session_t* s, char** b, size_t* bl, mpack_data_t d)

    int mpack_rpc_reply(mpack_rpc_session_t* s, char** b, size_t* bl, mpack_uint32_t i)

    int mpack_rpc_notify(mpack_rpc_session_t* s, char** b, size_t* bl)

    void mpack_rpc_session_copy(mpack_rpc_session_t* d, mpack_rpc_session_t* s)

    cdef enum:
        MPACK_RPC_RECEIVE_ARRAY
        MPACK_RPC_RECEIVE_TYPE
        MPACK_RPC_RECEIVE_ID

    mpack_rpc_header_t mpack_rpc_request_hdr()

    mpack_rpc_header_t mpack_rpc_reply_hdr()

    mpack_rpc_header_t mpack_rpc_notify_hdr()

    int mpack_rpc_put(mpack_rpc_session_t* s, mpack_rpc_message_t m)

    int mpack_rpc_pop(mpack_rpc_session_t* s, mpack_rpc_message_t* m)

    void mpack_rpc_reset_hdr(mpack_rpc_header_t* hdr)
